import Input from './Input'
import Modal from './Modal'
import Spinner from './Spinner'

const UIPlugin = {
  install: Vue => {
    [
      Input,
      Modal,
      Spinner
    ].forEach(component => {
      Vue.component(component.name, component)
    })
  }
}

export default UIPlugin
