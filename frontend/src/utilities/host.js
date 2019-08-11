const host = () => {
  return window.location.host.split('.')
}

export default {
  isAdmin: () => host().length === 1,
  getSubdomain: () => host()[0]
}
