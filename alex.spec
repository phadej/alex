%define name    alex
%define version 2.0
%define release 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        BSD-like
Group:          Development/Languages/Haskell
URL:            http://haskell.org/alex/
Source:         http://haskell.org/alex/dist/%{version}/alex-%{version}-src.tar.gz
Packager:       Sven Panne <sven.panne@aedion.de>
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Prefix:         %{_prefix}
BuildRequires:  happy, ghc, docbook-dtd, docbook-xsl-stylesheets, libxslt, libxml2, fop, xmltex, dvips
Summary:        The lexer generator for Haskell

%description
Alex is a tool for generating lexical analysers in Haskell, given a
description of the tokens to be recognised in the form of regular
expressions.  It is similar to the tool lex or flex for C/C++.

%prep
%setup -n alex-%{version}

%build
test -f configure || autoreconf
./configure --prefix=%{prefix}
make
make html

%install
make prefix=${RPM_BUILD_ROOT}%{prefix} install

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc alex/ANNOUNCE
%doc alex/LICENSE
%doc alex/README
%doc alex/TODO
%doc alex/doc/alex
%doc alex/examples
%{prefix}/bin/alex
%{prefix}/bin/alex-%{version}
%{prefix}/lib/alex-%{version}