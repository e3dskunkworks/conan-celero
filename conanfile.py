from conans import ConanFile, CMake, tools

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

class CeleroConan(ConanFile):
    name = "Celero"
    version = "2.1"
    license = "Apache License Version 2.0"
    url = "Go to https://github.com/DigitalInBlue/Celero-Conan for a real recipie once 2.1.1 is released"
    description = "C++ Benchmark Authoring Library/Framework"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        gitRepo = "https://github.com/DigitalInBlue/Celero.git"
        self.run("git clone %s" % (gitRepo))
        self.run("cd Celero && git checkout")
        
    def build(self):
        cmake = CMake(self)
        if self.options.shared:
            cmake.definitions["CELERO_COMPILE_DYNAMIC_LIBRARIES"] = "ON"
        else:
            cmake.definitions["CELERO_COMPILE_DYNAMIC_LIBRARIES"] = "OFF"
        cmake.definitions["CELERO_ENABLE_EXPERIMENTS"] = "OFF"
        cmake.definitions["CELERO_ENABLE_FOLDERS"] = "OFF"
        cmake.configure()
        cmake.build(target="celero")
        cmake.install()


    def package(self):
        self.copy("*", src="package")

        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["celero"]
        self.cpp_info.libdirs = ["lib","lib/static","bin"]
