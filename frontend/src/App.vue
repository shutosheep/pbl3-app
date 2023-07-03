<template>
  <div style="height:600px; width:800px">
    <l-map ref="map" v-model:zoom="zoom" :use-global-leaflet="false" :center="center">
      <l-tile-layer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        layer-type="base"
        name="OpenStreetMap"
      />
      <l-marker v-for='i in vendingmachine' @click="clickMarker(i.id)" :lat-lng="i.location" ></l-marker>
    </l-map>
  </div>
  <div>
    {{ vendingmachine }}
    <br>
    {{ menu }}
  </div>
</template>

<script>
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LMarker } from "@vue-leaflet/vue-leaflet";
import axios from 'axios';

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
  },
  data() {
    return {
      zoom: 15,
      center: [34.982155233542514, 135.9635035902881], // university
      vendingmachine: [],
      menu: [],
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:5000/")
      .then((response) => (this.vendingmachine = response.data))
      .catch(error => console.log(error))
  },
  methods: {
    clickMarker(id) {
      console.log("clicked! " + id)
      axios
        .get("http://127.0.0.1:5000/menu?id=" + id)
        .then((response) => (this.menu = response.data))
        .catch(error => console.log(error))
    }
  },
};
</script>

<style></style>
