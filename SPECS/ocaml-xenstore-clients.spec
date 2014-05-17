%global debug_package %{nil}

Name:           ocaml-xenstore-clients
Version:        0.9.3
Release:        1%{?dist}
Summary:        Unix xenstore clients for OCaml
License:        LGPL
Group:          Development/Libraries
URL:            https://github.com/xapi-project/ocaml-xenstore-clients
Source0:        https://github.com/xapi-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-xenstore-devel

%description
Unix xenstore clients for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-lwt-devel%{?_isa}
Requires:       ocaml-xenstore-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=${buildroot}


%files
#This space intentionally left blank

%files devel
%doc README.md LICENSE MAINTAINERS
%{_libdir}/ocaml/xenstore_transport/*

%changelog
* Fri May  9 2014 David Scott <dave.scott@citrix.com> - 0.9.3-1
- Update to 0.9.3

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.2-1
- Update to 0.9.2

* Mon Jun  3 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

