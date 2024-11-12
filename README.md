# micrograd

A tiny Autograd engine. Implements backpropagation (reverse-mode autodiff) over a dynamically built DAG and a small neural networks library on top of it with a PyTorch-like API. Both are tiny, with about 100 and 50 lines of code respectively. The DAG only operates over scalar values, so e.g. we chop up each neuron into all of its individual tiny adds and multiplies. However, this is enough to build up entire deep neural nets doing binary classification, as the demo notebook shows.

## Setup

(taken from [this project](https://github.com/suasuasuasuasua/project-euler))

Follow the instructions from [`devenv`](https://devenv.sh/getting-started/)
using the instructions found here.

### Install `nix`

```bash
### Via https://zero-to-nix.com/start/install (recommended)
curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install

### Via https://devenv.sh/getting-started/
## Linux
sh <(curl -L https://nixos.org/nix/install) --daemon

## macOS
curl -L https://raw.githubusercontent.com/NixOS/experimental-nix-installer/main/nix-installer.sh | sh -s install

## WSL2
sh <(curl -L https://nixos.org/nix/install) --no-daemon
```

### Install `devenv`

```bash
## General
nix-env -iA devenv -f https://github.com/NixOS/nixpkgs/tarball/nixpkgs-unstable

## NixOS
# Add the following to your configuration.nix somewhere
environment.systemPackages = [ 
  pkgs.devenv
];
```

#### `devenv.nix`

Defines the configuration for the `devenv` shell. This is where we define all
the tooling, packages, scripts, services, processes, etc. that we need for the
project.

#### `devenv.yaml`

The `yaml` defines the sources for all the packages, i.e. where are we getting
the cached builds or build instructions for `nix`.

## Usage

Call `devenv shell` to install all the project dependencies specified in
`./devenv.nix`, then spawn a development shell with all the proper
dependencies set up.

Source your environment, spin up a notebook and start developing:

```
jupyter notebook --ip 0.0.0.0 --port 8888 --no-browser
```
