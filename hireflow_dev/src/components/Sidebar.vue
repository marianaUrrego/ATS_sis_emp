<script setup>
//import { HomeIcon, BriefcaseIcon, FileTextIcon, LogOutIcon } from "lucide-vue-next";
</script>

<template>
  <aside class="w-64 h-screen bg-black text-white flex flex-col">
    <div class="flex items-center justify-center h-20 border-b border-gray-700">
      <span
        class="w-16 h-16 flex items-center justify-center text-3xl font-bold bg-white text-black rounded-full"
        >H</span
      >
    </div>

    <nav class="flex-1 mt-4 space-y-2">
      <router-link
        to="/"
        class="flex items-center space-x-3 px-6 py-3 text-gray-300 hover:bg-gray-800 transition"
      >
        <HomeIcon class="w-5 h-5" />
        <span>Home</span>
      </router-link>

      <router-link
        to="/jobs"
        class="flex items-center space-x-3 px-6 py-3 text-gray-300 hover:bg-gray-800 transition"
      >
        <BriefcaseIcon class="w-5 h-5" />
        <span>Ofertas de trabajo</span>
      </router-link>

      <router-link
        to="/resumes"
        class="flex items-center space-x-3 px-6 py-3 text-gray-300 hover:bg-gray-800 transition"
      >
        <FileTextIcon class="w-5 h-5" />
        <span>Hojas de vida</span>
      </router-link>

      <router-link
        to="/logout"
        class="flex items-center space-x-3 px-6 py-3 text-gray-300 hover:bg-gray-800 transition"
      >
        <LogOutIcon class="w-5 h-5" />
        <span>Cerrar sesión</span>
      </router-link>
    </nav>
  </aside>
</template>
