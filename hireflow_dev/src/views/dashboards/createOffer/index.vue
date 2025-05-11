<script setup lang="ts">
import { ref } from 'vue';
/* Breadcrumb component */
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';

import UiParentCard from '@/components/shared/UiParentCard.vue';

/*Call Components*/
import CardsDashboard from '@/components/dashboards/dashboard2/CardsDashboard.vue';
import TableOffer from '@/components/table/TableOffer.vue';
import RequerimentsCard from '@/components/dashboards/dashboard2/RequerimentsCard.vue';
import RequerimentsCard2 from '@/components/dashboards/dashboard2/RequirementsCardsText.vue';
// template breadcrumb
const page = ref({ title: 'Crear oferta' });
const breadcrumbs = ref([
    {
        text: 'Home',
        disabled: false,
        href: '#'
    },
    {
        text: 'Oferta',
        disabled: true,
        href: '#'
    }
]);

</script>
<template>
    <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
    
</template>
