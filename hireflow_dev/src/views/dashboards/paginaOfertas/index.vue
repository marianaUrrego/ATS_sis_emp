<script setup lang="ts">
import { ref,onMounted, computed } from 'vue';
import IntroOferta from '@/components/dashboards/paginaOfertas/IntroOferta.vue';
import { useRouter } from 'vue-router';
const router = useRouter();

interface Card {
  id: string
  nombre: string;
  departamento: string;
  fecha_creacion: string;
}
const cards = ref<Card[]>([])  // ahora es un ref reactivo

const departamentos = ref<Array<{ id: number; nombre: string }>>([]);
const depaSeleccionado = ref<string | null>(null);

onMounted(async () => {
  try {
    // obtener las ofertas
    const response = await fetch('http://127.0.0.1:8000/ofertas/')
    if (!response.ok) throw new Error('Error al cargar ofertas')
    const data = await response.json()
    cards.value = data

     // Obtener los departamentos
    const resDepartamentos = await fetch('http://127.0.0.1:8000/ofertas/departamentos/')
    if (!resDepartamentos.ok) throw new Error('Error al cargar departamentos')
    const dataDepartamentos = await resDepartamentos.json()
    departamentos.value = dataDepartamentos

  } catch (error) {
    console.error('Error al obtener los datos:', error)
  }
})

const ofertasFiltradas = computed(() => {
  if (!depaSeleccionado.value) return cards.value;
  
  return cards.value.filter(oferta => 
    oferta.departamento === depaSeleccionado.value
  );
});

</script>
<template>
  <h3 class="display-1 textPrimary font-weight-bold" style="margin-bottom: 20px;">Ofertas de trabajo</h3>
  <v-row>
    <v-col>
      <v-select 
        v-model="depaSeleccionado"
        :items="departamentos"
        item-title="nombre"
        item-value="nombre"
        label="Departamento"
        clearable
      ></v-select>
    </v-col>
    <v-col>
      <div class="ml-auto">
        <v-btn color="primary"@click="router.push('/dashboards/createOffer')">Crear nueva oferta</v-btn>
      </div>
    </v-col>
  </v-row>
  <v-row dense>
    <v-col
      v-for="(card, index) in ofertasFiltradas"
      :key="index"
      cols="12"
      sm="6"
      md="6"
      lg="4"
    >
      <IntroOferta
        @click="router.push({ name: 'DetalleOferta', params: { id: card.id } })"
        :nombreOferta="card.nombre"
        :departamento="card.departamento"
        :fechaCreacion="card.fecha_creacion"
      />
    </v-col>
  </v-row>
</template>