# TODO: systam upb and utf8_range?
Summary:	Python bindings for Protocol Buffers
Summary(pl.UTF-8):	Wiązania Pythona do buforów protokołowych (Protocol Buffers)
Name:		python3-protobuf
Version:	7.34.1
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/protobuf/
Source0:	https://files.pythonhosted.org/packages/source/p/protobuf/protobuf-%{version}.tar.gz
# Source0-md5:	7d860558dfbd2762140370c391285c35
URL:		https://pypi.org/project/protobuf/
BuildRequires:	python3-modules >= 1:3.10
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for Protocol Buffers.

Protocol Buffers are Google's data interchange format.

%description -l pl.UTF-8
Wiązania Pythona do buforów protokołowych (Protocol Buffers).

Protocol Buffers to format wymiany danych stworzony przez Google.

%prep
%setup -q -n protobuf-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitedir}/google
%dir %{py3_sitedir}/google/_upb
%attr(755,root,root) %{py3_sitedir}/google/_upb/_message.cpython-*.so
%{py3_sitedir}/google/protobuf
%{py3_sitedir}/protobuf-%{version}-py*.egg-info
