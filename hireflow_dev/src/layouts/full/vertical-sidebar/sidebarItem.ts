
export interface menu {
    header?: string;
    title?: string;
    icon?: any;
    to?: string;
    chip?: string;
    BgColor?: string;
    chipBgColor?: string;
    chipColor?: string;
    chipVariant?: string;
    chipIcon?: string;
    children?: menu[];
    disabled?: boolean;
    type?: string;
    subCaption?: string;
}
//Aqui agarra los iconos de solar
const sidebarItem: menu[] = [
    { header: 'DASHBOARDS' },
    {
        title: 'Home',
        icon: 'home-2-line-duotone',
        to: '/dashboards/dashboard1'
    },
    {
        title: 'Oferta de trabajo',
        icon: 'letter-linear',
        to: '/dashboards/dashboard2'
    },
    {
        title: 'Ofertas de trabajo',
        icon: 'letter-linear',
        to: '/dashboards/paginaOfertas'
    },
    {
        title: 'Hojas de vida',
        icon: 'user-id-line-duotone',
        to: '/dashboards/dashboard3'
    },
    { header: 'APPS' },
    {
        title: 'User Profile',
        icon: 'shield-user-line-duotone',
        to: '/',
        children: [
            {
                title: 'Profile',
                to: '/apps/user/profile'
            },
        ]
    },
    {
        title: 'Tickets',
        icon: 'ticker-star-outline',
        to: '/apps/tickets'
    },
    { header: 'PAGES' },
    {
        title: 'Account Setting',
        icon: 'settings-minimalistic-line-duotone',
        to: '/pages/account-settings'
    },
    {
        title: 'Banners Widgets',
        icon: 'align-vertical-spacing-line-duotone',
        to: '/widgets/banners'
    },
    {
        title: 'Cards Widgets',
        icon: 'cardholder-line-duotone',
        to: '/widgets/cards'
    },
    {
        title: 'Charts Widgets',
        icon: 'chart-square-line-duotone',
        to: '/widgets/charts'
    },
    {
        title: 'Landing Page',
        icon: 'passport-line-duotone',
        to: '/'
    },

    { header: 'UI' },
    {
        title: 'UI Elements',
        icon: 'waterdrops-line-duotone',
        to: '#',
        children: [
            {
                title: 'Alert',
                to: '/ui-components/alert'
            },
            {
                title: 'Accordion',
                to: '/ui-components/accordion'
            },
            {
                title: 'Avatar',
                to: '/ui-components/avatar'
            },
            {
                title: 'Chip',
                to: '/ui-components/chip'
            },
            {
                title: 'Dialog',
                to: '/ui-components/dialogs'
            },
            {
                title: 'List',
                to: '/ui-components/list'
            },
            {
                title: 'Menus',
                to: '/ui-components/menus'
            },
            {
                title: 'Tabs',
                to: '/ui-components/tabs'
            },
            {
                title: 'Tooltip',
                to: '/ui-components/tooltip'
            },
            {
                title: 'Typography',
                to: '/ui-components/typography'
            }
        ]
    },

    { header: 'Forms' },
    {
        title: 'Form Elements',
        icon: 'text-selection-line-duotone',
        to: '/components/',
        children: [
            {
                title: 'Autocomplete',
                to: '/forms/form-elements/autocomplete'
            },
            {
                title: 'Combobox',
                to: '/forms/form-elements/combobox'
            },
            {
                title: 'Button',
                to: '/forms/form-elements/button'
            },
            {
                title: 'Checkbox',
                to: '/forms/form-elements/checkbox'
            },
            {
                title: 'Custom Inputs',
                to: '/forms/form-elements/custominputs'
            },
            {
                title: 'File Inputs',
                to: '/forms/form-elements/fileinputs'
            },
            {
                title: 'Radio',
                to: '/forms/form-elements/radio'
            },
            {
                title: 'Date Time',
                to: '/forms/form-elements/date-time'
            },
            {
                title: 'Select',
                to: '/forms/form-elements/select'
            },
            {
                title: 'Slider',
                to: '/forms/form-elements/slider'
            },
            {
                title: 'Switch',
                to: '/forms/form-elements/switch'
            },
            {
                title: 'Time Picker',
                to: '/forms/form-elements/time-picker'
            },
            {
                title: 'Stepper',
                to: '/forms/form-elements/stepper'
            }
        ]
    },
    {
        title: 'Form Layout',
        icon: 'layers-minimalistic-outline',
        to: '/forms/form-layouts'
    },
    {
        title: 'Form Horizontal',
        icon: 'password-minimalistic-input-line-duotone',
        to: '/forms/form-horizontal'
    },
    {
        title: 'Form Vertical',
        icon: 'slider-vertical-line-duotone',
        to: '/forms/form-vertical'
    },
    {
        title: 'Form Custom',
        icon: 'clapperboard-play-outline',
        to: '/forms/form-custom'
    },
    {
        title: 'Form Validation',
        icon: 'soundwave-square-line-duotone',
        to: '/forms/form-validation'
    },
    {
        title: 'Editor',
        icon: 'clapperboard-edit-line-duotone',
        to: '/forms/editor'
    },

    { header: 'Tables' },
    {
        title: 'Basic Table',
        icon: 'tablet-line-duotone',
        to: '/tables/basic'
    },
    {
        title: 'Dark Table',
        icon: 'bedside-table-4-outline',
        to: '/tables/dark'
    },
    {
        title: 'Density Table',
        icon: 'bedside-table-3-linear',
        to: '/tables/density'
    },
    {
        title: 'Fixed Header Table',
        icon: 'archive-up-minimlistic-broken',
        to: '/tables/fixed-header'
    },
    {
        title: 'Height Table',
        icon: 'archive-down-minimlistic-broken',
        to: '/tables/height'
    },
    {
        title: 'Editable Table',
        icon: 'document-add-linear',
        to: '/tables/editable'
    },


    { header: 'Data Tables' },
    {
        title: 'Basic Table',
        icon: 'database-outline',
        to: '/tables/datatables/basic'
    },
    {
        title: 'Header Table',
        icon: 'folder-open-broken',
        to: '/tables/datatables/header'
    },
    {
        title: 'Selection Table',
        icon: 'chart-square-broken',
        to: '/tables/datatables/selection'
    },
    {
        title: 'Sorting Table',
        icon: 'card-send-line-duotone',
        to: '/tables/datatables/sorting'
    },
    {
        title: 'Pagination Table',
        icon: 'tag-horizontal-broken',
        to: '/tables/datatables/pagination'
    },
    {
        title: 'Filtering Table',
        icon: 'tuning-square-2-line-duotone',
        to: '/tables/datatables/filtering'
    },
    {
        title: 'Grouping Table',
        icon: 'tuning-square-2-line-duotone',
        to: '/tables/datatables/grouping'
    },
    {
        title: 'Table Slots',
        icon: 'closet-line-duotone',
        to: '/tables/datatables/slots'
    },
    {
        title: 'CRUD Table',
        icon: 'text-underline-cross-broken',
        to: '/tables/datatables/crudtable'
    },

    { header: 'Auth' },
    {
        title: 'Error',
        icon: 'bug-minimalistic-line-duotone',
        to: '/auth/404'
    },
    {
        title: 'Side Login',
        icon: 'login-3-line-duotone',
        to: '/auth/login'
    },
    {
        title: 'Boxed Login',
        icon: 'login-3-line-duotone',
        to: '/auth/login2'
    },
    {
        title: 'Side Register',
        icon: 'user-plus-rounded-line-duotone',
        to: '/auth/register'
    },
    {
        title: 'Boxed Register',
        icon: 'user-plus-rounded-line-duotone',
        to: '/auth/register2'
    },
    {
        title: 'Side Forgot Pwd',
        icon: 'password-outline',
        to: '/auth/forgot-password'
    },
    {
        title: 'Boxed Forgot Pwd',
        icon: 'password-outline',
        to: '/auth/forgot-password2'
    },
    {
        title: 'Side Two Steps',
        icon: 'siderbar-line-duotone',
        to: '/auth/two-step'
    },
    {
        title: 'Boxed Two Steps',
        icon: 'siderbar-line-duotone',
        to: '/auth/two-step2'
    },

    { header: 'ICONS' },
    {
        title: 'Solar Icons',
        icon: 'sticker-smile-circle-2-line-duotone',
        to: '/icons/solar'
    },

];

export default sidebarItem;
