<template>
  <div class="row">
    <div class="col-md-12">
      <div id="carousel" class="carousel slide" data-ride="carousel">
        <ol class="carousel-indicators">
          <li data-target="#carousel" data-slide-to="0" class="active"></li>
          <li data-target="#carousel" data-slide-to="1"></li>
          <li data-target="#carousel" data-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
          <div class="item active">
            <img
              src="http://placehold.it/2000x800/39CCCC/ffffff&text=Acetaminofen"
              alt="Acetaminofen"
            >
          </div>
          <div class="item">
            <img
              src="http://placehold.it/2000x800/45AB23/ffffff&text=Loratadina"
              alt="Loratadina"
            >
          </div>
          <div class="item">
            <img
              src="http://placehold.it/2000x800/AA44CC/ffffff&text=Dolex"
              alt="Dolex"
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'carousel'
}
</script>
