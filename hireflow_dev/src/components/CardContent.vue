<script setup>
import { ref } from 'vue'
import CardStat from './CardStat.vue'
import checkGreen from '../assets/icons/check-green.png'
import alertYellow from '../assets/icons/alert-yellow.png'
import cancelRed from '../assets/icons/cancel-red.png'
import cvPurple from '../assets/icons/CV-purple.png'

const cardsData = ref([
  {
    id: 1,
    title: 'Aceptados',
    figure: '28',
    cardImage: checkGreen,
  },
  {
    id: 2,
    title: 'Por revisar',
    figure: '14',
    cardImage: alertYellow,
  },
  {
    id: 3,
    title: 'Rechazados',
    figure: '12',
    cardImage: cancelRed,
  },
  {
    id: 4,
    title: 'Fase de pruebas',
    figure: '28',
    cardImage: cvPurple,
  },
])
</script>

<template>
  <div
    class="max-w-6xl flex-grow mx-auto min-h-[400px] bg-white rounded-lg shadow-lg border border-gray-200"
  >
    <div class="grid grid-cols-4 gap-6 mx-6 my-6">
      <CardStat v-for="card in cardsData" :key="card.id" :cardData="card" />
    </div>
  </div>
</template>
