
%define with_python3 0
%if 0%{?fedora} > 18
%define with_python3 1
%endif

Summary: The libvirt virtualization API python2 binding
Name: libvirt-python
Version: 1.2.1
Release: 2%{?dist}%{?extra_release}
Source0: http://libvirt.org/sources/python/%{name}-%{version}.tar.gz
Url: http://libvirt.org
License: LGPLv2+
Group: Development/Libraries
BuildRequires: libvirt-devel >= 0.9.11
BuildRequires: python-devel
%if %{with_python3}
BuildRequires: python3-devel
%endif

%if %{with_python3}
%package -n libvirt-python3
Summary: The libvirt virtualization API python3 binding
Url: http://libvirt.org
License: LGPLv2+
Group: Development/Libraries
%endif

# Don't want provides for python shared objects
%{?filter_provides_in: %filter_provides_in %{python_sitearch}/.*\.so}
%{?filter_setup}

%description
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).

%if %{with_python3}
%description -n libvirt-python3
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).
%endif

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build
%if %{with_python3}
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
%endif

%install
%{__python} setup.py install --skip-build --root=%{buildroot}
%if %{with_python3}
%{__python3} setup.py install --skip-build --root=%{buildroot}
%endif
rm -f %{buildroot}%{_libdir}/python*/site-packages/*egg-info

%files
%defattr(-,root,root)
%doc ChangeLog AUTHORS NEWS README COPYING COPYING.LESSER examples/
%{_libdir}/python2*/site-packages/libvirt.py*
%{_libdir}/python2*/site-packages/libvirt_qemu.py*
%{_libdir}/python2*/site-packages/libvirtmod*

%if %{with_python3}
%files -n libvirt-python3
%defattr(-,root,root)
%doc ChangeLog AUTHORS NEWS README COPYING COPYING.LESSER examples/
%{_libdir}/python3*/site-packages/libvirt.py*
%{_libdir}/python3*/site-packages/libvirt_qemu.py*
%{_libdir}/python3*/site-packages/__pycache__/libvirt.cpython-*.py*
%{_libdir}/python3*/site-packages/__pycache__/libvirt_qemu.cpython-*.py*
%{_libdir}/python3*/site-packages/libvirtmod*
%endif

%changelog
* Tue May  6 2014 David Scott <dave.scott@citrix.com> - 1.2.1-2
- Remove dependency on LXC

* Tue May  6 2014 David Scott <dave.scott@citrix.com> - 1.2.1-1
- Import package from libvirt.org
