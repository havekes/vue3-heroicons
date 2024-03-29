# Vue 3 Heroicons components

## Update 2021-05-08

Upstream (https://github.com/tailwindlabs/heroicons) has now a Vue component library.
I'm archiving this repo in favor of the official library.



Heroicons components for Vue 3 with TypeScript typings.

Version of this package will follow the Heroicons versions.

## Usage

```
npm i @havekes/vue3-heroicons
yarn add @havekes/vue3-heroicons
```

In a component:

```js
// ...
import { OPlus } from '@havekes/vue3-heroicons';

export default defineComponent({
  components: { OPlus }
  // ...
})
```

For now, the library is only built as an ESM bundle.

## Updating from upstream and compiling

The `make_library.py` script will regenerate all icons from the [heroicons repo](https://github.com/tailwindlabs/heroicons).
It requires the request Python package to be installed.

```
pip install requests
python make_library.py
yarn build
```
