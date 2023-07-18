<template>
  <Navbar />
  <v-container>
    <v-row align-content="center">
      <v-col>
        <h1 class="text-h3 font-weight-medium my-6">Info</h1>
        <div class="d-flex">
          <div>
            <h2 class="text-h4 font-weight-medium my-4">Getting started</h2>
            <p class="my-2 text-body-1">
              Are you the first time to use this app? Here are some steps you
              want to follow.
              <br />
              For general information on our project, please take a look at our
              <a href="http://shutosheep.github.io/pbl3-website"
                >project website.</a
              >
              <br />
              The image on the right is the icon of our app.
            </p>
          </div>
          <v-img class="ml-8 mt-4" :max-width="150" src="/icon.png"></v-img>
        </div>
        <h3 class="text-h5 font-weight-medium my-4">
          1. Select vending machine
        </h3>
        <p class="my-2 text-body-1">
          Select one of the vending machine on the map. You can see the menu by
          looking at the table on the right.
        </p>
        <h3 class="text-h5 font-weight-medium my-4">
          2. Filter by type and value
        </h3>
        <p class="my-2 text-body-1">
          Apply filtering by selecting Filter type. Input filter value acording
          to the filter type you have chosen.
          <br />
          If filter type is product name, input the product name which you want
          to filter. It is recommended to copy paste the product name on the
          table.
          <br />
          If filter type id price, input the minimum price which you want to
          filter. It fill filter the vending machines which only contains the
          product that are under the inputted price.
          <br />
          Press the filter button to filter.
        </p>
        <h3 class="text-h5 font-weight-medium my-4">
          3. View the filtered result
        </h3>
        <p class="my-2 text-body-1">
          The filtered vending machines will be shown on the map. Note that the
          filtered item will be in red color in the table on right.
          <br />
          <b
            >If you don't see any vending machines on the map, check the filter
            value which you input.</b
          >
        </p>
        <h3 class="text-h5 font-weight-medium my-4">4. Choose random menu</h3>
        <p class="my-2 text-body-1">
          You can choose random vending machine menu using the button.
          <br />
          Have fun with the roulette. :D
        </p>
        <h2 class="text-h4 font-weight-medium my-4">
          Interested in developing?
        </h2>
        <p class="my-2 text-body-1">
          Our application is open source! Source code is avilable on
          <a href="https://github.com/shutosheep/pbl3-app">Github</a>.
          <br />
          This application uses Flask, Python for backend API server and Vue,
          Vuetify, Node.js for frontend.
        </p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Navbar from "./Navbar.vue";

export default {
  components: {
    Navbar,
  },
};
</script>
