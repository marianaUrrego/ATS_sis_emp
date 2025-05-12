
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
    {
        title: 'Crear oferta',
        icon: 'user-id-line-duotone',
        to: '/dashboards/createOffer'
    },

];

export default sidebarItem;
