from conans import ConanFile, CMake, tools
import os

class ZlibConan(ConanFile):
    name = "zlib"
    version = "1.2.11"
    author = "Ralph-Gordon Paul (gordon@rgpaul.com)"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False],
                "android_ndk": "ANY"}
    default_options = "shared=False", "android_ndk=None"
    description = "Compressing File-I/O Library"
    url = "https://github.com/Manromen/conan-zlib-scripts"
    license = "Zlib"

    # download zlib sources
    def source(self):
        url = "https://zlib.net/zlib%s.zip" % self.version.replace(".","")
        tools.get(url)

    # compile using cmake
    def build(self):
        cmake = CMake(self)
        zlib_folder = "%s/zlib-%s" % (self.source_folder, self.version)
        cmake.verbose = True
        cmake.configure(source_folder=zlib_folder)
        cmake.build()
        cmake.install()

        if self.settings.os == "Windows":
            libname = "zlib"
            static_libname = "zlibstatic"
            if self.settings.build_type == "Debug":
                libname = "zlibd"
                static_libname = "zlibstaticd"

            # delete shared artifacts for static builds and the static library for shared builds
            if self.options.shared == False:
                os.remove('%s/bin/%s.dll' % (self.package_folder, libname))
                os.remove('%s/lib/%s.lib' % (self.package_folder, libname))
                os.rename('%s/lib/%s.lib' % (self.package_folder, static_libname), '%s/lib/%s.lib' % (self.package_folder, libname))
            else:
                os.remove('%s/lib/%s.lib' % (self.package_folder, static_libname))        

    def package(self):
        self.copy("*", dst="include", src='include')
        self.copy("*.lib", dst="lib", src='lib', keep_path=False)
        self.copy("*.dll", dst="bin", src='bin', keep_path=False)
        self.copy("*.so", dst="lib", src='lib', keep_path=False)
        self.copy("*.dylib", dst="lib", src='lib', keep_path=False)
        self.copy("*.a", dst="lib", src='lib', keep_path=False)
        
    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.includedirs = ['include']

    def config_options(self):
        # remove android specific option for all other platforms
        if self.settings.os != "Android":
            del self.options.android_ndk
