<template>
  <div class="flex">
    <div class="map">
      <l-map ref="map" v-model:zoom="zoom" :use-global-leaflet="false" :center="center">
        <l-tile-layer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          layer-type="base"
          name="OpenStreetMap"
        />
        <l-marker v-for='i in vendingmachine' @click="clickMarker(i.id)" :lat-lng="i.location" ></l-marker>
      </l-map>
    </div>
    <div class="right">
      <VendingInfo :menu=menu :location=location />
    </div>
  </div>
</template>

<script>
import "./style/global.scss";
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LMarker } from "@vue-leaflet/vue-leaflet";
import axios from 'axios';
import VendingInfo from './components/VendingInfo.vue';

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    VendingInfo,
  },
  data() {
    return {
      zoom: 15,
      center: [34.982155233542514, 135.9635035902881], // university
      vendingmachine: null,
      menu: null,
      location: null,
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
      axios
        .get("http://127.0.0.1:5000/location?id=" + id)
        .then((response) => (this.location = response.data))
        .catch(error => console.log(error))
    }
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
