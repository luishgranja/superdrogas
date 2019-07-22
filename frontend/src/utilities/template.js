export default {
  refresh: () => {
    // eslint-disable-next-line
    $(function () {
      // eslint-disable-next-line
      $('#table').DataTable({
        'retrieve': true
      })
    })
  },
  hideModal: (modalName) => {
    // eslint-disable-next-line
    $(modalName).modal('hide')
  }
}
