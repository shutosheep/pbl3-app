<template>
  <div class="flex">
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
            {{ i.location }}
          </l-popup>
        </l-marker>
      </l-map>
    </div>
    <div class="right">
      <h1>Vendeye</h1>
      <div>
        <h2>Filter by...</h2>
        <p>
          Filter type:
          <select v-model="filterType">
            <option v-for="i in filterTypeOptions">
              {{ i }}
            </option>
          </select>
        </p>
        <p v-if="filterType != filterTypeOptions[2]">
          Filter value:
          <input type="text" v-model="filterValue" />
        </p>
        <button @click="clickResetFilter()">Reset filter!</button>
        <button @click="clickFilter(filterType, filterValue)">Filter!</button>
      </div>
      <VendingInfo :menu="menu" />
    </div>
  </div>
</template>

<script>
import "./style/global.scss";
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LMarker, LPopup } from "@vue-leaflet/vue-leaflet";
import axios from "axios";
import VendingInfo from "./components/VendingInfo.vue";

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
      zoom: 15,
      center: [34.982155233542514, 135.9635035902881], // university
      vendingmachine: null,
      menu: null,
      filterType: null,
      filterTypeOptions: ["Name", "Price", "Cacheless payment avilable"],
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
    },
    clickFilter(filterType, filterValue) {
      if (filterType == null) {
        alert("Please choose filter type!");
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
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.flex {
  display: flex;
}

.map {
  width: 1024px;
  height: 720px;
}

.right {
  margin-left: 1rem;
}
</style>
