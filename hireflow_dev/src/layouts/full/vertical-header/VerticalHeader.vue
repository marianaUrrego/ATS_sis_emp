<script setup lang="ts">
import { ref, watch, computed } from 'vue';
import { useCustomizerStore } from '../../../stores/customizer';
import { useEcomStore } from '@/stores/apps/eCommerce';
import ProfileDD from './ProfileDD.vue';
import RightMobileSidebar from './RightMobileSidebar.vue';
import { Icon } from '@iconify/vue';
import Logo from '../logo/Logo.vue';
import ThemeToggler from './ThemeToggler.vue';
const customizer = useCustomizerStore();
const priority = ref(customizer.setHorizontalLayout ? 0 : 0);

watch(priority, (newPriority) => {
    priority.value = newPriority;
});

</script>

<template>
    <v-app-bar elevation="0" :priority="priority" height="70" id="top" class="main-head">
        <v-btn
            class="hidden-md-and-down custom-hover-primary" icon
            size="small" variant="text" color="primary"
            @click.stop="customizer.SET_MINI_SIDEBAR(!customizer.mini_sidebar)"
        >
            <Icon icon="solar:hamburger-menu-line-duotone" height="22"   />
        </v-btn>

        <v-btn class="hidden-lg-and-up custom-hover-primary" size="small" variant="text" color="primary" icon  @click.stop="customizer.SET_SIDEBAR_DRAWER" >
            <Icon icon="solar:hamburger-menu-line-duotone" height="22"   />
        </v-btn>

        <v-spacer class="hidden-sm-and-down" />

        <!-- ---------------------------------------------- -->
        <!-- Mobile Logo -->
        <!-- ---------------------------------------------- -->
        <div class="hidden-md-and-up">
            <Logo />
        </div>

        <!-- ThemeToggler -->
        <ThemeToggler/>
        
        <!-- ---------------------------------------------- -->
        <!-- User Profile -->
        <!-- ---------------------------------------------- -->
        <div class="hidden-sm-and-down">
            <ProfileDD />
        </div>

        <!----Mobile ----->
        <v-menu :close-on-content-click="true" class="mobile_popup ">
                    <template v-slot:activator="{ props }">
                        <v-btn icon class="hidden-md-and-up custom-hover-primary"  color="primary" variant="text" v-bind="props" size="small">
                            <Icon icon="solar:menu-dots-bold-duotone" height="22"   />
                        </v-btn>
                    </template>
                    <v-sheet rounded="lg" elevation="10" class="mt-4 dropdown-box px-4 py-3">
                        <div class="d-flex justify-space-between align-center">
                            <RightMobileSidebar/>
                            <ProfileDD />
                        </div>
                    </v-sheet>
                </v-menu>
    </v-app-bar>
</template>
