<script setup>
import { ref, computed } from 'vue'
import { filterCompStyles } from '@/constants/filterCompStyles'
const states = ['no-filter', 'high-to-low', 'low-to-high']
const currentState = ref(states[0])

const getUpArrowClass = computed(() => {
  switch (currentState.value) {
    case states[0]:
      return filterCompStyles.noFilterUp
    case states[1]:
      return filterCompStyles.highToLowUp
    case states[2]:
      return filterCompStyles.lowToHighUp
    default:
      return filterCompStyles.noFilterUp // Default fallback
  }
})

const getDownArrowClass = computed(() => {
  switch (currentState.value) {
    case states[0]:
      return filterCompStyles.noFilterDown
    case states[1]:
      return filterCompStyles.highToLowDown
    case states[2]:
      return filterCompStyles.lowToHighDown
    default:
      return filterCompStyles.noFilterDown // Default fallback
  }
})

const toggleFilter = () => {
  const currentIndex = states.indexOf(currentState.value)
  const nextIndex = (currentIndex + 1) % states.length
  currentState.value = states[nextIndex]
}
</script>

<template>
  <div @click="toggleFilter" class="max-w-24 -mt-[1px] flex flex-col cursor-pointer">
    <img src="../assets/icons/filterup-black.png" alt="" :class="getUpArrowClass" />
    <img src="../assets/icons/filterdown-black.png" alt="" :class="getDownArrowClass" />
  </div>
</template>
