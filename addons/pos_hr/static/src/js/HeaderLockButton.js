odoo.define('point_of_sale.HeaderLockButton', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const { useState } = owl;

    class HeaderLockButton extends PosComponent {
        constructor() {
            super(...arguments);
            this.stop_barcode = new ProductScreen();
            this.state = useState({ isUnlockIcon: true, title: 'Unlocked' });
        }
        async showLoginScreen() {

            this.stop_barcode._stopcustomBarcodeScanner();
            await this.showTempScreen('LoginScreen');
        }
        onMouseOver(isMouseOver) {
            this.state.isUnlockIcon = !isMouseOver;
            this.state.title = isMouseOver ? 'Lock' : 'Unlocked';
        }
    }

    Registries.Component.add(HeaderLockButton);

    return HeaderLockButton;
});
