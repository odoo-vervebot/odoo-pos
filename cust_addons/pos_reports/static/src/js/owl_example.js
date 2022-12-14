const { Component, mount, xml, useState, onWillRender, onPatched} = owl;

// -----------------------------------------------------------------------------
// Data generation
// -----------------------------------------------------------------------------

let idCounter = 1;
const adjectives = [
    "pretty", "large", "big", "small", "tall", "short", "long", "handsome", "plain",
    "quaint", "clean", "elegant", "easy", "angry", "crazy", "helpful", "mushy", "odd",
    "unsightly", "adorable", "important", "inexpensive", "cheap", "expensive", "fancy"];
const colours = ["red", "yellow", "blue", "green", "pink", "brown", "purple", "brown", "white", "black", "orange"];
const nouns = ["table", "chair", "house", "bbq", "desk", "car", "pony", "cookie", "sandwich", "burger", "pizza", "mouse", "keyboard"];

function _random (max) { return Math.round(Math.random() * 1000) % max; };

function buildData(count) {
    const data = new Array(count);
    for (let i = 0; i < count; i++) {
        const label = `${adjectives[_random(adjectives.length)]} ${colours[_random(colours.length)]} ${nouns[_random(nouns.length)]}`;
        data[i] = {
            id: idCounter++,
            label,
        };
    }
    return data;
}

// -----------------------------------------------------------------------------
// Components
// -----------------------------------------------------------------------------
class Button extends Component {
  static template = xml`
      <div class='col-sm-6 smallpad'>
          <button t-att-id="props.id" class='btn btn-primary btn-block' type='button' t-on-click="props.onClick">
              <t t-esc="props.text"/>
          </button>
      </div>`;
}


class Row extends Component {
  static template = xml`
      <tr t-att-class="props.isSelected ? 'danger' : ''">
          <td class="col-md-1" t-esc="props.row.id" />
          <td class="col-md-4">
              <a t-on-click="() => props.onSelect(props.row.id)" t-esc="props.row.label" />
          </td>
          <td class="col-md-1">
              <a t-on-click="() =>  props.onRemove(props.row.id)" class="remove">[x]
                <span class='glyphicon glyphicon-remove' aria-hidden="true" />
              </a>
          </td>
          <td class='col-md-6'/>
      </tr>`
}

class Root extends Component {
  static template = xml`
      <div class='container'>
        <div class='jumbotron'>
          <div class='row'>
            <div class='col-md-6'>
              <h1>Owl Keyed</h1>
            </div>
            <div class='col-md-6'>
              <div class='row'>
                <Button id="'run'" onClick.bind="run" text="'Create 1,000 rows'" />
                <Button id="'runlots'" onClick.bind="runLots" text="'Create 10,000 rows'" />
                <Button id="'add'" onClick.bind="add" text="'Append 1,000 rows'" />
                <Button id="'update'" onClick.bind="update" text="'Update every 10th row'" />
                <Button id="'clear'" onClick.bind="clear" text="'Clear'" />
                <Button id="'swaprows'" onClick.bind="swapRows" text="'Swap Rows'" />
              </div>
            </div>
          </div>
        </div>
        <table class='table table-hover table-striped test-data'>
          <tbody>
            <t t-foreach="state.rows" t-as="row" t-key="row.id">
                <Row row="row" isSelected="row.id === state.selectedRowId" onSelect.bind="selectRow" onRemove.bind="removeRow"/>
            </t>
          </tbody>
        </table>
        <span class='preloadicon glyphicon glyphicon-remove' aria-hidden="true" />
      </div>`;

  static components = { Button, Row };

  setup() {
      this.state = useState({
          rows: [],
          selectedRowId: null
      });
      this.benchmarking = false;
      onPatched(() => {
          if (this.benchmarking) {
              this.stop();
          }
      });
    }

    start(descr) {
        this.benchmarking = `[${descr}]`;
        console.time(this.benchmarking);
    }
    stop() {
        console.timeEnd(this.benchmarking);
        this.benchmarking = false;
    }

    run() {
        this.start('add1000');
        this.state.rows = buildData(1000);
        this.state.selectedRowId = null;
    }

    runLots() {
        this.start('add10_000');
        this.state.rows = buildData(10_000);
        this.state.selectedRowId = null;
    }

    add() {
        this.start('append1000');
        this.state.rows = this.state.rows.concat(buildData(1000));
    }

    update() {
        this.start('update1/10th');
        let index = 0;
        const rows = this.state.rows;
        while (index < rows.length) {
            rows[index].label = rows[index].label + " !!!";
            index += 10;
        }
    }

    clear() {
        this.start('clear');
        this.state.rows = [];
        this.state.selectedRowId = null;
    }

    swapRows() {
        this.start('swap');
        const rows = this.state.rows;
        if (rows.length > 998) {
            let tmp = rows[1];
            rows[1] = rows[998];
            rows[998] = tmp;
        }
    }

    selectRow(id) {
        this.start('select');
        this.state.selectedRowId = id;
    }

    removeRow(id) {
        this.start('remove1');
        const rows = this.state.rows;
        rows.splice(rows.findIndex(row => row.id === id), 1);
    }
}


mount(Root, document.body, { templates: TEMPLATES, dev: true });