<script setup lang="ts">
import { ref } from 'vue';
/* Breadcrumb component */
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';

import UiParentCard from '@/components/shared/UiParentCard.vue';

import { BasicDatatables } from '@/_mockApis/components/datatable/dataTable';

/*Call Components*/
import ProfitCard from '@/components/dashboards/dashboard2/ProfitCard.vue';
import SubscriptionCard from '@/components/dashboards/dashboard2/SubscriptionCard.vue';
import UsersChart from '@/components/dashboards/dashboard2/UsersChart.vue';

import CardsDashboard from '@/components/dashboards/dashboard2/CardsDashboard.vue';


// template breadcrumb
const page = ref({ title: 'Nombre de la oferta' });
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

/*Header Data*/
const search = ref();
const customsearch = ref();
const headers: any = ref([
    { title: 'Aplicante', align: 'start', key: 'name' },
    { title: 'Fecha de envío', align: 'start', key: 'project' },
    { title: 'Post', align: 'start', key: 'post' },
    { title: 'Status', align: 'start', key: 'status' },
    { title: 'Budget', align: 'end', key: 'budget' },
])

const expanded = ref();
const headersExpand: any = ref([
    { title: 'Aplicante', align: 'start', key: 'name', sortable: false, },
    { title: 'Fecha de envío', align: 'start', key: 'fecha' },
    { title: 'Post', align: 'start', key: 'post' },
    { title: 'Status', align: 'start', key: 'status' },
    { title: 'Budget', align: 'end', key: 'budget' },
    { title: '', key: 'data-table-expand' },
])


/*for status color*/
function getColor(status: string) {
    if (status == 'Active') return '#13DEB9'
    else if (status == 'Cancel') return '#FA896B'
    else if (status == 'Completed') return '#5D87FF'
    else return '#FFAE1F'
}

const filtrable = ref('')

function filterOnlyCapsText(value: { toString: () => string; } | null, query: string | null, item: any) {
    return value != null &&
        query != null &&
        typeof value === 'string' &&
        value.toString().toLocaleUpperCase().indexOf(query) !== -1
}
</script>
<template>
    <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
    <v-row>
        <v-col cols="12" xl="5" class="py-3 pl-6 pr-4 d-flex align-center">
            <v-row>
                <h3 class="display-1 textPrimary font-weight-bold ">Developer</h3>
            </v-row>
            <div class="ml-auto">
                <v-btn color="primary">Crear nueva oferta</v-btn>
            </div>
        </v-col>

        <v-row>
            <!-- Subscription -->
            <v-col cols="12" md="4">
                <SubscriptionCard />
            </v-col>
            <!-- Users -->
            <v-col cols="12" md="4">
                <UsersChart />
            </v-col>
            <!-- Users -->
            <v-col cols="12" md="4">
                <UsersChart />
            </v-col>
        </v-row>
        <!-- Profit card -->
        <v-col cols="12" lg="6">
            <ProfitCard />
        </v-col>
        <!-- Profit card -->
        <v-col cols="12" lg="6">
            <ProfitCard />
        </v-col>

        <!-- ---------------------------------------------------- -->
        <!-- Table -->
        <!-- ---------------------------------------------------- -->
        <v-col cols="12">
            <UiParentCard title="Aplicantes a la oferta">
                <v-text-field v-model="search" append-inner-icon="mdi-magnify" label="Search" single-line hide-details
                    class="mb-5" />
                <v-data-table items-per-page="5" :headers="headers" :items="BasicDatatables" :search="search"
                    class="border rounded-md datatabels">
                    <template v-slot:item.status="{ item }">
                        <v-chip :color="getColor(item.status)">
                            {{ item.status }}
                        </v-chip>
                    </template>
                </v-data-table>
            </UiParentCard>
        </v-col>
        <DefaultLayout>
            <CardsDashboard />
        </DefaultLayout>
    </v-row>
</template>
