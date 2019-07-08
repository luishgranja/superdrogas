export default {
  refresh: () => {
    // eslint-disable-next-line
    $(function () { $('#table').DataTable() })
  },
  hideModal: (modalName) => {
    // eslint-disable-next-line
    $(modalName).modal('hide')
  }
}
