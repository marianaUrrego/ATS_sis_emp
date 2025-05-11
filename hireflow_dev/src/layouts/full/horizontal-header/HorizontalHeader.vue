<script setup lang="ts">
import { ref, watch} from 'vue';
import { useCustomizerStore } from '../../../stores/customizer';
import Logo from '../logo/Logo.vue';
// dropdown imports
import ProfileDD from '../vertical-header/ProfileDD.vue';
import Navigations from '../vertical-header/Navigations.vue';
import RightMobileSidebar from '../vertical-header/RightMobileSidebar.vue';
import { Icon } from '@iconify/vue';
import ThemeToggler from '../vertical-header/ThemeToggler.vue';
const customizer = useCustomizerStore();

const priority = ref(customizer.setHorizontalLayout ? 0 : 0);

watch(priority, (newPriority) => {
    // yes, console.log() is a side effect
    priority.value = newPriority;
});

</script>

<template>
    <v-app-bar elevation="0" :priority="priority" height="70" id="top" class="horizontal-header border-b">
        <div :class="customizer.boxed ? 'maxWidth v-toolbar__content' : 'v-toolbar__content px-6'">
            <div class="hidden-md-and-down">
                <Logo />
            </div>
            <v-btn class="hidden-lg-and-up ms-3" icon rounded="sm" variant="text"   @click.stop="customizer.SET_SIDEBAR_DRAWER" size="small">
                <Icon icon="solar:hamburger-menu-line-duotone" height="22" />
            </v-btn>

            <!-- ------------------------------------------------>
            <!-- Mega menu -->
            <!-- ------------------------------------------------>
            <div class="hidden-sm-and-down">
                <Navigations />
            </div>

            <v-spacer class="hidden-sm-and-down" />
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
            <v-menu :close-on-content-click="true" class="mobile_popup">
                <template v-slot:activator="{ props }">
                    <v-btn icon class="hidden-md-and-up custom-hover-primary" color="primary" variant="text" v-bind="props" size="small">
                        <Icon icon="solar:menu-dots-bold-duotone" height="22" />
                    </v-btn>
                </template>
                <v-sheet rounded="lg" elevation="10" class="mt-4 dropdown-box px-4 py-3">
                    <div class="d-flex justify-space-between align-center">
                        <RightMobileSidebar />
                        <!-- <MessagesDD /> -->
                        <ProfileDD />
                    </div>
                </v-sheet>
            </v-menu>
        </div>
    </v-app-bar>
</template>
