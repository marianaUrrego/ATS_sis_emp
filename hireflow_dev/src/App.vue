<script setup>
import TableComp from './components/TableComp.vue'
import ButtonComp from './components/ButtonComp.vue'
import downloadBlue from './assets/icons/search-blue.png'
const headers = [
  {
    key: 'name',
    label: 'Aplicantes',
    hasFilter: true,
    centered: 'false',
    rowType: 'textMedium',
    width: '300px',
  },
  {
    key: 'fechaEnvio',
    label: 'Fecha de envío',
    hasFilter: true,
    centered: 'true',
    rowType: 'text',
    width: '170px',
  },
  {
    key: 'archivo',
    label: 'Archivo',
    hasFilter: false,
    centered: 'true',
    rowType: 'button',
    width: '200px',
  },
  {
    key: 'estado',
    label: 'Estado',
    hasFilter: true,
    centered: 'true',
    rowType: 'state',
    width: '170px',
  },
  {
    key: 'oferta',
    label: 'Oferta',
    hasFilter: false,
    centered: 'true',
    rowType: 'textUnderscore',
  },
]

const dataset = [
  {
    name: 'Alfonso Gabriel Jiménez Rivas',
    fechaEnvio: '10/MAR/2025',
    archivo: 'Ver Archivo',
    estado: 'aceptado',
    oferta: '123 Main St',
  },
  {
    name: 'Juana Jaramillo Montoya',
    fechaEnvio: '10/MAR/2025',
    archivo: 'Ver Archivo',
    estado: 'rechazado',
    oferta: '456 Oak Ave',
  },
  {
    name: 'Mariana Lizette Urrego Montoya',
    fechaEnvio: '10/MAR/2025',
    archivo: 'Ver Archivo',
    estado: 'por revisar',
    oferta: '789 Pine Rd',
  },
]
</script>

<template>
  <TableComp :columns="headers" :data="dataset" />
  <ButtonComp
    buttonText="Ver Archivo"
    buttonType="BigSquareButtonImgLeft"
    :buttonImage="downloadBlue"
  />
</template>
