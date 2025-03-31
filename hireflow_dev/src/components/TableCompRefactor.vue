<script setup>
import { defineProps } from 'vue'
import { thStyles, tdStyles, divStyles } from '@/constants/tableStyles'
import ButtonComp from './ButtonComp.vue'
import State from './State.vue'
import FilterComp from './FilterComp.vue'

defineProps({
  columns: {
    type: Array,
    required: true,
    // Example: [{key: 'name', label: 'Name', hasFilter: 'true', centered: 'false', rowType: 'button'},
    // {key: 'fechaEnvio', label: 'Fecha de envío', hasFilter: 'true', centered: 'true', rowType: 'text'},
    // {key: 'fechaEnvio', label: 'Fecha de envío', hasFilter: 'true', centered: 'false', rowType: 'state'}]
    // Por ahora las rows sólo pueden ser de tipo button, text, textMedium, textUnderscore o state.
    // Los styles son llamados con el mismo nombre de key, están en constants/tableStyles.js
  },
  data: {
    type: Array,
    required: true,
    default: () => [],
  },
})
</script>

<template>
  <div class="max-w-5xl w-full">
    <table class="w-full border-collapse border-spacing-0 table-fixed">
      <thead class="border border-color-[#E9ECEF]">
        <tr>
          <!--Selecciona un thStyle en función del nombre de key al concatenarle Th-->
          <th :class="thStyles[col.key + 'Th']" v-for="col in columns" :key="col.key">
            <!--Centra la columna en caso de que su atributo centered sea true-->
            <div :class="[col.centered === 'true' ? divStyles.alignCenter : divStyles.alignLeft]">
              {{ col.label }}
              <FilterComp v-if="col.hasFilter" />
            </div>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr class="border border-b-[#E9ECEF]" v-for="(row, index) in data" :key="index">
          <!--Selecciona un tdStyle en función del nombre de key-->
          <td :class="tdStyles[col.rowType]" v-for="col in columns" :key="col.key">
            <template v-if="col.rowType === 'button'">
              <!--Añade un button si el header indica que esta es una fila archivo-->
              <ButtonComp :buttonText="row[col.key]" buttonType="MdSquareButton" />
            </template>
            <template v-else-if="col.rowType === 'state'">
              <!--Añade un State si el header indica que esta es una columna estado-->
              <State :estado="row[col.key]" />
            </template>
            <template v-else>
              <!--En cualquier otro caso, imprime normalmente el texto que trae la data de la columna-->
              {{ row[col.key] }}
            </template>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
