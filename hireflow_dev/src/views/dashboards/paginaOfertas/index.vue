<script setup lang="ts">
import { ref,onMounted } from 'vue';
import IntroOferta from '@/components/dashboards/paginaOfertas/IntroOferta.vue';
const cards = [
  {
    nombreOferta: 'coordinador de logistica',
    departamento: 'Logística',
    fechaCreacion: '01/04/2024'
  },
  {
    nombreOferta: 'reclutador de planta operativa',
    departamento: 'Recursos Humanos',
    fechaCreacion: '15/03/2023'
  },
  {
    nombreOferta: 'encargado de seguridad',
    departamento: 'Tecnología',
    fechaCreacion: '22/11/2022'
  }
]

const departamentos = ref(['Finanzas', 'Recursos Humanos', 'Logística', 'Tecnología', 'Ventas']);
const depaSeleccionado = ref()

</script>
<template>
    <h3 class="display-1 textPrimary font-weight-bold " style="margin-bottom: 20px;">Ofertas de trabajo</h3>
    <v-row>
        <v-col>
            <v-select v-model="depaSeleccionado" :items="departamentos" label="Departamento"></v-select>
        </v-col>
        <v-col>
            <div class="ml-auto text-right align-center">
            <v-btn color="primary">Crear nueva oferta</v-btn>
        </div>
        </v-col>
    </v-row>
    <v-row dense>
    <v-col
      v-for="(card, index) in cards"
      :key="index"
      cols="12"
      sm="6"
      md="6"
      lg="4"
    >
      <IntroOferta
        :nombreOferta=card.nombreOferta
        :departamento = card.departamento
        :fechaCreacion = card.fechaCreacion
      />
    </v-col>
  </v-row>

</template>