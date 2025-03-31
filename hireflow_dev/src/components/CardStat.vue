<script setup>
import LabelColor from './LabelColor.vue'
defineProps({
  cardData: {
    type: Object,
    required: true,
    validator: (obj) => {
      return obj.title && obj.figure && obj.cardImage
    },
  },
})
</script>

<template>
  <div class="rounded-lg border border-gray-200 p-4">
    <div class="flex flex-row justify-between">
      <div>
        <h2 class="text-xl font-500 font-[Inter] mb-1 text-[#9CA9B8]">{{ cardData.title }}</h2>
        <div class="text-[24px] font-[Inter] font-bold text-[#3E3E67] mb-[30px]">
          {{ cardData.figure }}
        </div>
      </div>
      <div>
        <img class="w-10 h-10" :src="cardData.cardImage" alt="" />
      </div>
    </div>
    <LabelColor figure="3.45%" text="desde el mes pasado" />
  </div>
</template>
