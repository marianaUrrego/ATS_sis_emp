<script setup lang="ts">

import { ref } from 'vue';

//Base de datos simulada
import { BasicDatatables } from '@/_mockApis/components/datatable/dataTable';


const search = ref();
const estadosSeleccionado = ref()
const estado = ref(['Activo', 'Por Revisar', 'Rechazados', 'Fase de prueba', 'Fase de entrevista', 'Finalistas']);
//Esta es la construcción de la tabla, en key toca mirar como traemos los datos reales
const headers : any = ref([
    { title: 'Aplicante', align: 'start', key: 'name' },
    { title: 'Fecha de envío', align: 'start', key: 'project' },
    { title: 'Archivo', align: 'start', key: 'post' },
    { title: 'Estado', align: 'start', key: 'status' },
    { title: 'Oferta', align: 'end', key: 'budget' },
    { title: 'Departamento', align: 'end', key: 'post' },
])

/*for status color*/
function getColor(status: string) {
    if (status == 'Active') return '#13DEB9'
    else if (status == 'Cancel') return '#FA896B'
    else if (status == 'Completed') return '#5D87FF'
    else return '#FFAE1F'
}
</script>
<template>
    <v-data-table items-per-page="5" :headers="headers" :items="BasicDatatables" :search="search"
        class="border rounded-md datatabels">
            <template v-slot:item.status="{ item }">
                    <v-chip :color="getColor(item.status)">
                        {{ item.status }}
                    </v-chip>
            </template>
    </v-data-table>
</template>