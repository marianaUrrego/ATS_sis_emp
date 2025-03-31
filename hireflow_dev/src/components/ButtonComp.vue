<script setup>
import { buttonStyles } from '@/constants/buttonStyles'
import { defineProps, ref, computed } from 'vue'

const isHovered = ref(false)

const props = defineProps({
  buttonText: String,
  buttonType: {
    type: String,
    required: true,
    validator: (value) => Object.keys(buttonStyles).includes(value),
  },
  buttonImage: {
    type: String,
    required: false,
  },
  plusImage: {
    type: Boolean,
    required: true,
  },
})

const imageSource = computed(() => {
  const shouldChangeOnHover = [
    'SmRoundButtonBorderImgLeft',
    'SmRoundButtonBorderImgRight',
  ].includes(props.buttonType)

  if (props.buttonImage && shouldChangeOnHover) {
    return isHovered.value
      ? props.buttonImage.replace('-blue.png', '-white.png')
      : props.buttonImage
  }
  return props.buttonImage
})
</script>

<template>
  <button
    :class="buttonStyles[buttonType]"
    @mouseenter="isHovered = true"
    @mouseleave="isHovered = false"
  >
    <img
      v-if="
        !plusImage &&
        buttonImage &&
        (buttonType === 'SmRoundButtonBorderImgLeft' ||
          buttonType === 'SmRoundButtonImgLeft' ||
          buttonType === 'BigSquareButtonImgLeft')
      "
      :src="imageSource"
      class="w-[12px] h-[12px] mr-1"
    />
    <span
      class="text-[16px] font-regular text-center mr-1 -mt-[3px]"
      v-if="
        plusImage &&
        (buttonType === 'SmRoundButtonBorderImgLeft' ||
          buttonType === 'SmRoundButtonImgLeft' ||
          buttonType === 'BigSquareButtonImgLeft')
      "
    >
      +
    </span>
    <span>{{ buttonText }}</span>
    <span
      class="text-[16px] font-regular text-center ml-1 -mt-[3px]"
      v-if="plusImage && buttonType === 'SmRoundButtonImgRight'"
      :src="buttonImage"
    >
      +
    </span>
    <img
      v-if="!plusImage && buttonImage && buttonType === 'SmRoundButtonBorderImgRight'"
      :src="imageSource"
      class="w-[12px] h-[12px] ml-1"
    />
  </button>
</template>

<style>
.rounded-15px {
  border-radius: 15px;
}
.rounded-5px {
  border-radius: 5px;
}
</style>
