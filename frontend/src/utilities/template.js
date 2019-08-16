/* eslint-disable */
export default {
  destroy: () => {
    $('#table').DataTable().destroy()
  },
  reload: () => {
    $('#table').DataTable()
  },
  hideModal: (modalName) => {
    $(modalName).modal('hide')
  }
}
