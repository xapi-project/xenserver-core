Name:           xcp-rrdd
Version:        0.9.1
Release:        1
Summary:        Statistics gathering daemon for the xapi toolstack
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xapi-project/xcp-rrdd/archive/%{version}.tar.gz
Source0:        https://github.com/xapi-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        xcp-rrdd-init
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-obuild ocaml-findlib ocaml-camlp4-devel
BuildRequires:  ocaml-xcp-idl-devel ocaml-syslog-devel ocaml-rpc-devel
BuildRequires:  ocaml-re-devel ocaml-cohttp-devel ocaml-xcp-inventory-devel
BuildRequires:  ocaml-xen-api-libs-transitional-devel
BuildRequires:  ocaml-xen-lowlevel-libs-devel
BuildRequires:  ocaml-xenops-devel
BuildRequires:  ocaml-oclock-devel
BuildRequires:  xen-devel message-switch-devel forkexecd-devel
Requires:       redhat-lsb-core

%description
Statistics gathering daemon for the xapi toolstack.

%prep
%setup -q
cp %{SOURCE1} xcp-rrdd-init

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
make install DESTDIR=%{buildroot} SBINDIR=%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 xcp-rrdd-init %{buildroot}%{_sysconfdir}/init.d/xcp-rrdd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.markdown LICENSE
%{_sbindir}/xcp-rrdd
%{_sysconfdir}/init.d/xcp-rrdd

%post
/sbin/chkconfig --add xcp-rrdd

%preun
if [ $1 -eq 0 ]; then
  /sbin/service xcp-rrdd stop > /dev/null 2>&1
  /sbin/chkconfig --del xcp-rrdd
fi

%changelog
* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.1

* Tue Jun 18 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

