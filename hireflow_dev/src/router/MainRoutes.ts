const MainRoutes = {
    path: '/main',
    meta: {
        requiresAuth: true
    },
    redirect: '/main',
    component: () => import('@/layouts/full/FullLayout.vue'),
    children: [
        {
            name: 'Dashboard1',
            path: '/dashboards/dashboard1',
            component: () => import('@/views/dashboards/dashboard1/index.vue')
        },
        {
            name: 'Dashboard2',
            path: '/dashboards/dashboard2',
            component: () => import('@/views/dashboards/dashboard2/index.vue')
        },
         {
            name: 'DetalleOferta',
            path: '/detalleOferta/:id',
            component: () => import('@/views/dashboards/dashboard2/index.vue')
        },
        {
            name: 'Dashboard3',
            path: '/dashboards/dashboard3',
            component: () => import('@/views/dashboards/dashboard3/index.vue')
        },
        {
            name: 'PaginaOfertas',
            path: '/dashboards/paginaOfertas',
            component: () => import('@/views/dashboards/paginaOfertas/index.vue')
        },
        
        {
            name: 'CreateOffer',
            path: '/dashboards/createOffer',
            component: () => import('@/views/dashboards/createOffer/index.vue')
        },
        {
            name: 'Banners',
            path: '/widgets/banners',
            component: () => import('@/views/widgets/banners/banners.vue')
        },
        {
            name: 'Cards',
            path: '/widgets/cards',
            component: () => import('@/views/widgets/cards/cards.vue')
        },
        {
            name: 'Charts',
            path: '/widgets/charts',
            component: () => import('@/views/widgets/charts/charts.vue')
        },
        {
            name: 'Autocomplete',
            path: '/forms/form-elements/autocomplete',
            component: () => import('@/views/forms/form-elements/VAutocomplete.vue')
        },
        {
            name: 'Combobox',
            path: '/forms/form-elements/combobox',
            component: () => import('@/views/forms/form-elements/Combobox.vue')
        },
        {
            name: 'File Inputs',
            path: '/forms/form-elements/fileinputs',
            component: () => import('@/views/forms/form-elements/FileInputs.vue')
        },
        {
            name: 'Custom Inputs',
            path: '/forms/form-elements/custominputs',
            component: () => import('@/views/forms/form-elements/CustomInputs.vue')
        },
        {
            name: 'Select',
            path: '/forms/form-elements/select',
            component: () => import('@/views/forms/form-elements/Select.vue')
        },
        {
            name: 'Button',
            path: '/forms/form-elements/button',
            component: () => import('@/views/forms/form-elements/VButtons.vue')
        },
        {
            name: 'Checkbox',
            path: '/forms/form-elements/checkbox',
            component: () => import('@/views/forms/form-elements/VCheckbox.vue')
        },
        {
            name: 'Radio',
            path: '/forms/form-elements/radio',
            component: () => import('@/views/forms/form-elements/VRadio.vue')
        },
        {
            name: 'Date Time',
            path: '/forms/form-elements/date-time',
            component: () => import('@/views/forms/form-elements/VDateTime.vue')
        },
        {
            name: 'Time Picker',
            path: '/forms/form-elements/time-picker',
            component: () => import('@/views/forms/form-elements/VTimePicker.vue')
        },

        {
            name: 'Stepper',
            path: '/forms/form-elements/stepper',
            component: () => import('@/views/forms/form-elements/VStepper.vue')
        },
        {
            name: 'Slider',
            path: '/forms/form-elements/slider',
            component: () => import('@/views/forms/form-elements/VSlider.vue')
        },
        {
            name: 'Switch',
            path: '/forms/form-elements/switch',
            component: () => import('@/views/forms/form-elements/VSwitch.vue')
        },
        {
            name: 'Form Layout',
            path: '/forms/form-layouts',
            component: () => import('@/views/forms/FormLayouts.vue')
        },
        {
            name: 'Form Horizontal',
            path: '/forms/form-horizontal',
            component: () => import('@/views/forms/FormHorizontal.vue')
        },
        {
            name: 'Form Vertical',
            path: '/forms/form-vertical',
            component: () => import('@/views/forms/FormVertical.vue')
        },
        {
            name: 'Form Custom',
            path: '/forms/form-custom',
            component: () => import('@/views/forms/FormCustom.vue')
        },
        {
            name: 'Form Validation',
            path: '/forms/form-validation',
            component: () => import('@/views/forms/FormValidation.vue')
        },
        {
            name: 'Editor',
            path: '/forms/editor',
            component: () => import('@/views/forms/plugins/editor/Editor.vue')
        },
        {
            name: 'Basic Table',
            path: '/tables/basic',
            component: () => import('@/views/tables/TableBasic.vue')
        },
        {
            name: 'Dark Table',
            path: '/tables/dark',
            component: () => import('@/views/tables/TableDark.vue')
        },
        {
            name: 'Density Table',
            path: '/tables/density',
            component: () => import('@/views/tables/TableDensity.vue')
        },
        {
            name: 'Fixed Header Table',
            path: '/tables/fixed-header',
            component: () => import('@/views/tables/TableHeaderFixed.vue')
        },
        {
            name: 'Height Table',
            path: '/tables/height',
            component: () => import('@/views/tables/TableHeight.vue')
        },
        {
            name: 'Editable Table',
            path: '/tables/editable',
            component: () => import('@/views/tables/TableEditable.vue')
        },
        {
            name: 'Basic Data Table',
            path: '/tables/datatables/basic',
            component: () => import('@/views/tables/datatables/BasicTable.vue')
        },
        {
            name: 'Header Data Table',
            path: '/tables/datatables/header',
            component: () => import('@/views/tables/datatables/HeaderTables.vue')
        },
        {
            name: 'Selection Data Table',
            path: '/tables/datatables/selection',
            component: () => import('@/views/tables/datatables/Selectable.vue')
        },
        {
            name: 'Sorting Data Table',
            path: '/tables/datatables/sorting',
            component: () => import('@/views/tables/datatables/SortingTable.vue')
        },
        {
            name: 'Pagination Data Table',
            path: '/tables/datatables/pagination',
            component: () => import('@/views/tables/datatables/Pagination.vue')
        },
        {
            name: 'Filtering Data Table',
            path: '/tables/datatables/filtering',
            component: () => import('@/views/tables/datatables/Filtering.vue')
        },
        {
            name: 'Grouping Data Table',
            path: '/tables/datatables/grouping',
            component: () => import('@/views/tables/datatables/Grouping.vue')
        },
        {
            name: 'Slots Data Table',
            path: '/tables/datatables/slots',
            component: () => import('@/views/tables/datatables/Slots.vue')
        },
        {
            name: 'CRUD Table',
            path: '/tables/datatables/crudtable',
            component: () => import('@/views/tables/datatables/CrudTable.vue')
        },
        {
            name: 'Alert',
            path: '/ui-components/alert',
            component: () => import('@/views/ui-elements/UiAlert.vue')
        },
        {
            name: 'Accordion',
            path: '/ui-components/accordion',
            component: () => import('@/views/ui-elements/UiExpansionPanel.vue')
        },
        {
            name: 'Avtar',
            path: '/ui-components/avatar',
            component: () => import('@/views/ui-elements/UiAvatar.vue')
        },
        {
            name: 'Chip',
            path: '/ui-components/chip',
            component: () => import('@/views/ui-elements/UiChip.vue')
        },
        {
            name: 'Dialog',
            path: '/ui-components/dialogs',
            component: () => import('@/views/ui-elements/UiDialog.vue')
        },
        {
            name: 'List',
            path: '/ui-components/list',
            component: () => import('@/views/ui-elements/UiList.vue')
        },
        {
            name: 'Menus',
            path: '/ui-components/menus',
            component: () => import('@/views/ui-elements/UiMenus.vue')
        },
        {
            name: 'Tabs',
            path: '/ui-components/tabs',
            component: () => import('@/views/ui-elements/UiTabs.vue')
        },
        {
            name: 'Tooltip',
            path: '/ui-components/tooltip',
            component: () => import('@/views/ui-elements/UiTooltip.vue')
        },
        {
            name: 'Typography',
            path: '/ui-components/typography',
            component: () => import('@/views/style-animation/Typography.vue')
        },
        {
            name: "Tabler",
            path: "/icons/tabler",
            component: () => import("@/views/icons/TablerIcons.vue"),
        },
        {
            name: "Iconify",
            path: "/icons/solar",
            component: () => import("@/views/icons/IconifyIcons.vue"),
        },

    ]
};

export default MainRoutes;
