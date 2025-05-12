import { CircleIcon, PointIcon } from 'vue-tabler-icons';

export interface menu {
    header?: string;
    title?: string;
    icon?: any;
    to?: string;
    divider?: boolean;
    chip?: string;
    chipColor?: string;
    chipVariant?: string;
    chipIcon?: string;
    children?: menu[];
    disabled?: boolean;
    subCaption?: string;
    class?: string;
    extraclass?: string;
    type?: string;
}

const horizontalItems: menu[] = [
    {
        title: 'Dashboard',
        icon: 'home-2-line-duotone',
        to: '#',
        children: [
            {
                title: 'Home',
                icon: 'home-2-line-duotone',
                to: '/dashboards/dashboard1'
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
            }
        ]
    }
];

export default horizontalItems;
