<script setup>
import { defineProps } from 'vue'
// Seleccionar un color de span entre los siguientes: [blue-span, green-span, purple-span, yellow-span, red-span]
defineProps({
  color: {
    type: String,
    default: 'blue-span', // Color por defecto si no se pasa un valor
  },
})
</script>

<template>
  <span class="span mx-1 my-1 px-1.5 py-0.5 font-medium me-2 text-center rounded-sm" :class="color">
    DEPARTAMENTO
  </span>
</template>

<style>
.span {
  font-family: 'Inter';
  font-weight: 400;
  font-size: 12px;
}

.green-span {
  background-color: #caf3e1;
  color: #1fb073;
}

.blue-span {
  background-color: #cadcf3;
  color: #1f5bb0;
}

.purple-span {
  background-color: #d3caf3;
  color: #4d1fb0;
}

.yellow-span {
  background-color: #f3e5ca;
  color: #b0841f;
}

.red-span {
  background-color: #f3caca;
  color: #b0261f;
}
</style>
