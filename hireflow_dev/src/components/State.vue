<script setup>
import { defineProps, computed } from 'vue'

const props = defineProps({
  estado: {
    type: String,
    required: true,
    validator: (value) => ['rechazado', 'aceptado', 'por revisar'].includes(value),
  },
})

// Mapa de colores según el estado
const colorMap = {
  rechazado: { circle: 'red-circle', text: 'red-font' },
  aceptado: { circle: 'green-circle', text: 'green-font' },
  'por revisar': { circle: 'bg-yellow-400', text: 'text-yellow-400' },
}

// Clases computadas para el círculo
const circleColorClass = computed(() => {
  return colorMap[props.estado]?.circle || ''
})

// Clases computadas para el texto
const textColorClass = computed(() => {
  return colorMap[props.estado]?.text || ''
})
</script>

<template>
  <div class="flex justify-center w-full">
    <div class="flex items-center min-w-[110px] w-[110px]">
      <div class="w-1.5 h-1.5 rounded-full mr-1.5 flex-shrink-0" :class="circleColorClass"></div>
      <span class="font-state" :class="textColorClass">
        {{ props.estado }}
      </span>
    </div>
  </div>
</template>

<style>
.font-state {
  font-family: 'Inter';
  font-weight: 400;
  font-size: 13px;
}
.red-font {
  color: #ff6b6b;
}
.green-font {
  color: #3dd695;
}
.red-circle {
  background-color: #ff6b6b;
}
.green-circle {
  background-color: #3dd695;
}
</style>
