import Input from './components/Input'
import Modal from './components/Modal'
import Spinner from './components/Spinner'

const TemplatePlugin = {
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

export default TemplatePlugin
