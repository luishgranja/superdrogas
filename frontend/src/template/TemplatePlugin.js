import Input from './components/Input'
import Modal from './components/Modal'
import Select2 from './components/Select2'
import Spinner from './components/Spinner'

const TemplatePlugin = {
  install: Vue => {
    [
      Input,
      Modal,
      Select2,
      Spinner
    ].forEach(component => {
      Vue.component(component.name, component)
    })
  }
}

export default TemplatePlugin
