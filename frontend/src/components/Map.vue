<template>
  <div class="d-flex">
    <div class="map">
      <l-map
        ref="map"
        v-model:zoom="zoom"
        :use-global-leaflet="false"
        :center="center"
      >
        <l-tile-layer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          layer-type="base"
          name="OpenStreetMap"
        />
        <l-marker
          v-for="i in vendingmachine"
          v-on:click="clickMarker(vendingmachine, i.id, filterType)"
          :lat-lng="i.location"
        >
          <l-popup>
            You clicked this!
            <br />
            id = {{ i.id }}
            <br />
            {{ i.location }}
            <br />
            <a
              v-bind:href="
                'https://map.google.com/?q=' +
                i.location[0] +
                ',' +
                i.location[1]
              "
            >
              Open location in Google Map
            </a>
          </l-popup>
        </l-marker>
      </l-map>
    </div>
    <div class="ml-4">
      <div class="d-flex">
        <div>
          <h2 class="text-h4 my-5">Filter by...</h2>
          <p>
            <v-select
              label="Filter type"
              :items="filterTypeOptions"
              v-model="filterType"
              @change="changeFilterType($event)"
            />
          </p>
          <p v-if="filterType != filterTypeOptions[2]">
            <v-text-field label="Filter value" v-model="filterValue" />
          </p>
          <p class="d-flex">
            <v-btn @click="clickFilter(filterType, filterValue)">
              Filter
            </v-btn>
            <v-btn @click="clickResetFilter()">Clear filter</v-btn>
          </p>
        </div>
        <VendingInfo
          class="ml-4"
          :menu="menu"
          :filterType="filterType"
          :filterTypeOptions="filterTypeOptions"
          :filterValue="filterValue"
        />
      </div>
    </div>
  </div>
</template>

<script>
import "../style/global.scss";
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LMarker, LPopup } from "@vue-leaflet/vue-leaflet";
import axios from "axios";
import VendingInfo from "./VendingInfo.vue";

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
    VendingInfo,
  },
  data() {
    return {
      zoom: 14,
      center: [34.99126, 135.957415],
      vendingmachine: null,
      menu: null,
      filterType: null,
      filterTypeOptions: [
        "Product name",
        "Price",
        "Cacheless payment is avilable",
      ],
      filterValue: null,
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:5000/")
      .then((response) => (this.vendingmachine = response.data))
      .catch((error) => console.log(error));
  },
  methods: {
    clickMarker(vendingmachine, id, filterType) {
      // i dont know why i have to do this to fix some weird error
      if (filterType !== null) {
        id = vendingmachine[id - 1]["id"];
      }

      console.log("id = " + id);

      axios
        .get("http://127.0.0.1:5000/menu?id=" + id)
        .then((response) => (this.menu = response.data))
        .catch((error) => console.log(error));
    },
    clickResetFilter() {
      axios
        .get("http://127.0.0.1:5000/")
        .then((response) => (this.vendingmachine = response.data))
        .catch((error) => console.log(error));
      this.menu = null;
    },
    clickFilter(filterType, filterValue) {
      if (filterType == null) {
        alert("Please choose filter type!");
        return;
      }

      if (filterType != this.filterTypeOptions[2] && filterValue == null) {
        alert("Please type filter value!");
        return;
      }

      if (filterType == this.filterTypeOptions[0]) {
        axios
          .get(
            "http://127.0.0.1:5000/filter?filter_type=name" +
              "&filter_value=" +
              filterValue,
          )
          .then((response) => (this.vendingmachine = response.data))
          .catch((error) => console.log(error));
      } else if (filterType == this.filterTypeOptions[1]) {
        axios
          .get(
            "http://127.0.0.1:5000/filter?filter_type=price" +
              "&filter_value=" +
              filterValue,
          )
          .then((response) => (this.vendingmachine = response.data))
          .catch((error) => console.log(error));
      } else if (filterType == this.filterTypeOptions[2]) {
        axios
          .get("http://127.0.0.1:5000/filter?filter_type=ict")
          .then((response) => (this.vendingmachine = response.data))
          .catch((error) => console.log(error));
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.map {
  width: 1000px;
  height: 900px;
}
</style>
