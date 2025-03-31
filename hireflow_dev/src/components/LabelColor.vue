<script setup>
defineProps({
  figure: String,
  text: String,
})
</script>
<template>
  <p class="text-gray-400 font-[Inter] font-light text-sm">
    <span class="text-[#2EEB9A]">{{ figure }}</span> {{ text }}
  </p>
</template>
