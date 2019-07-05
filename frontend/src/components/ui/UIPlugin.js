import Modal from './Modal'
import Spinner from './Spinner'

const UIPlugin = {
  install: Vue => {
    [
      Modal,
      Spinner
    ].forEach(component => {
      Vue.component(component.name, component)
    })
  }
}

export default UIPlugin
