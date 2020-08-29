import navbar from './navbar';

export default {
    title: 'Components',
  };

  export const navBar = () => ({
    components: { navbar },
    template: '<navbar></navbar>'
})