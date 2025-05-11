<script setup lang="ts">

import { ref } from 'vue';

/* Breadcrumb component */
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import TableApplicants from '@/components/table/TableApplicants.vue';
// template breadcrumb
const page = ref({ title: '' });
const breadcrumbs = ref([
    {
        text: 'Home',
        disabled: false,
        href: '#'
    },
    {
        text: 'Aplicantes',
        disabled: true,
        href: '#'
    }
]);
</script>
<template>
    <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
    <v-row>
        <v-col cols="12" xl="5" class="py-3 pl-6 pr-4 d-flex align-center mb-5">
                <v-row>
                    <h3 class="display-1 textPrimary font-weight-bold ">Hojas de vida</h3>
                </v-row>
        </v-col>
        <!-- ---------------------------------------------------- -->
        <!-- Table -->
        <!-- ---------------------------------------------------- -->
        <v-col cols="12">
                <TableApplicants/>
        </v-col>
    </v-row>
</template>
