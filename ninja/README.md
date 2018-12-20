## Ninja
Ninja is a small build system with a focus on speed. More details, source code, and installation instruction can be found [here](https://ninja-build.org) and also on [github](https://github.com/ninja-build/ninja).

>Note: ```ninja``` does not work for Fortan. To use ```ninja```, switch off Fortran.

>Hint: To disable Fortran in [Trilinos](github.com:trilinos/Trilinos.git), add ```-D Trilinos_ENABLE_Fortran:BOOL=OFF``` to the ```cmake``` command in your configure script.

### Installation
For installation of ```ninja```, follow the instructions on [here](https://ninja-build.org)

### Configure your code to use ```ninja```
Add the option ```-GNinja``` to the ```cmake``` command in your configure script.

#### Colored compiler output
Configure colored compiler output by adding a flag to your `CMAKE_CXX_FLAGS`:

- For Gnu's `gcc`, add compiler flag `-fdiagnostics-color=always`. 
- For Clang,  add compiler flag `-fcolor-diagnostics`. 

Refer to [this blog post](https://medium.com/@alasher/colored-c-compiler-output-with-ninja-clang-gcc-10bfe7f2b949) for further details and some CMake code snipptes to automate this in your CMake configuration.

### Using ```ninja```
To build your code, ```cd``` to top level directory of your build folder and type ```ninja -j numProc``` with ```numProc``` being the number of processes to be used for the build.

> Note: ```ninja -j numProc``` needs to be issued in the top level directory of your build folder. To be able to issue a biuld command from any subdirectory in the build folder, use ```ninjac -j numProc``` instead.
