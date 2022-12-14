/** @odoo-module **/

import { registry } from "@web/core/registry";
import { KeepLast } from "@web/core/utils/concurrency";
import { useService } from "@web/core/utils/hooks";
import { XMLParser } from "@web/core/utils/xml";
import { Model, useModel } from "@web/views/helpers/model";
import { ViewLayout } from "@web/views/view_layout";

// -----------------------------------------------------------------------------

class ListModel extends Model {
  static services = ["orm"];

  setup(params, { orm }) {
    this.model = params.resModel;
    this.columns = params.columns;
    this.orm = orm;
    this.keepLast = new KeepLast();
  }

  async load(params) {
    const fields = this.columns.map((col) => col.name);
    this.data = await this.keepLast.add(
      this.orm.searchRead(this.model, params.domain, fields, { limit: 40 })
    );
    this.notify();
  }
}

// -----------------------------------------------------------------------------

class ListArchParser extends XMLParser {
  parse(arch) {
    const columns = [];
    this.visitXML(arch, (node) => {
      if (node.tagName === "field") {
        columns.push({
          type: "field",
          name: node.getAttribute("name"),
        });
      }
    });
    return { columns };
  }
}

// -----------------------------------------------------------------------------

class ListView extends owl.Component {
  static type = "list";
  static display_name = "List";
  static icon = "fa-list-ul";
  static multiRecord = true;
  static components = { ViewLayout };

  static template = owl.tags.xml/* xml */ `
    <ViewLayout ViewClass="constructor">
      <table class="o_list table table-sm table-hover">
        <tbody class="ui-sortable">
          <tr t-foreach="model.data" t-as="record" t-key="record.id" class="o_data_row">
            <t t-foreach="archInfo.columns" t-as="column" t-key="column_index">
              <td class="o_data_cell" t-on-click="openRecord(record)">
                <t t-esc="record[column.name]"/>
              </td>
            </t>
          </tr>
        </tbody>
      </table>
    </ViewLayout>`;

  setup() {
    this.archInfo = new ListArchParser().parse(this.props.arch);
    this.actionService = useService("action");
    this.model = useModel(ListModel, {
      resModel: this.props.resModel,
      columns: this.archInfo.columns,
      domain: this.props.domain,
    });
  }

  openRecord(record) {
    const resIds = this.model.data.map((record) => record.id);
    this.actionService.switchView("form", { resId: record.id, resIds });
  }
}

registry.category("views").add("list", ListView);