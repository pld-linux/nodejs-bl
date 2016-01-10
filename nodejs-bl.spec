#
# Conditional build:
%bcond_with	tests		# build with tests

%define		pkg	bl
Summary:	A Node.js Buffer list collector, reader and streamer
Name:		nodejs-%{pkg}
Version:	0.9.0
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	https://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	0b654b2070b835ea9ea5cfac6254101e
URL:		https://github.com/rvagg/bl
BuildRequires:	rpmbuild(macros) >= 1.634
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	npm(hash_file)
BuildRequires:	npm(readable-stream)
BuildRequires:	npm(tape)
%endif
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bl is a storage object for collections of Node Buffers, exposing them
with the main Buffer readable API. Also works as a duplex stream so
you can collect buffers from a stream that emits them and emit buffers
to a stream that consumes them!

%prep
%setup -qc
mv package/* .

%build
%if %{with tests}
node test/test.js
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr package.json *.js $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
