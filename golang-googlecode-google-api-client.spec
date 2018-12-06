# Run tests in check 
%bcond_without check

# http://github.com/google/google-api-go-client
%global forgeurl        https://github.com/google/google-api-go-client
%global goipath         google.golang.org/api
%global commit          511bab8e55decfbe784cd2d1868fa5cda62dc6c1
%global gname           golang-google-golang-org-api

%gometa

Name:           golang-googlecode-google-api-client
Version:        0
Release:        0.28%{?dist}
Summary:        Go libraries for "new style" Google APIs
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}

%package -n %{gname}-devel
Summary:        Go libraries for "new style" Google APIs
BuildArch:      noarch

BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/context/ctxhttp)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/sync/semaphore)
BuildRequires: golang(google.golang.org/appengine)
BuildRequires: golang(google.golang.org/appengine/socket)
BuildRequires: golang(google.golang.org/appengine/urlfetch)
BuildRequires: golang(google.golang.org/genproto/googleapis/bytestream)
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: golang(google.golang.org/grpc/codes)
BuildRequires: golang(google.golang.org/grpc/credentials)
BuildRequires: golang(google.golang.org/grpc/credentials/oauth)
BuildRequires: golang(google.golang.org/grpc/naming)

%if %{with check}
BuildRequires: golang(github.com/google/go-cmp/cmp)
%endif

%description -n %{gname}-devel
%{summary}

These are auto-generated Go libraries from the Google Discovery Services JSON
description files of the available "new style" Google APIs.

Announcement email:
http://groups.google.com/group/golang-nuts/browse_thread/thread/6c7281450be9a21e

Status: Relative to the other Google API clients, this library is labeled alpha.
Some advanced features may not work. Please file bugs if any problems are found.

Getting started documentation:
    http://code.google.com/p/google-api-go-client/wiki/GettingStarted 

%prep
%forgesetup

%install
%goinstall

%if %{with check}
%check
%gochecks
%endif

%files  -n %{gname}-devel -f devel.file-list
%license LICENSE
%doc README.md GettingStarted.md CONTRIBUTORS CONTRIBUTING.md AUTHORS

%changelog
* Sat Oct 27 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.28.20181027git511bab8
- Bump to upstream 511bab8e55decfbe784cd2d1868fa5cda62dc6c1

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.27.git9c79dee
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26.git9c79dee
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.25.2018417git9c79dee
- Bump to upstream 9c79deebf7496e355d7e95d82d4af1fe4e769b2f
  related: #1250521

* Thu Apr 19 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.24.gite6586c9
- Provide support/bundler as well
  related: #1250521

* Mon Apr 16 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.23.gite6586c9
- Patch formatting errors
- Remove code.google.com/api

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.gite6586c9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.21.gite6586c9
- Bump to upstream e6586c9293b9d514c7f5d5076731ec977cff1be6
  related: #1250521

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.git77f162b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.19.git77f162b
- Bump to upstream 77f162b8178853926ec7d7673e1aa77f8128517a
  related: #1250521

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.gite6294e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.gite6294e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.16.gite6294e6
- Bump to upstream e6294e63a06b2be522ff3d328d8cacded0b1bd31
  related: #1250521

* Thu Dec 15 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.16.git18450f4
- Polish the spec file
  related: #1250521

* Tue Aug 09 2016 jchaloup <jchaloup@redhat.com> - 0-0.15.git18450f4
- Polish spec file, enable devel and unit-test for epel7
  related: #1250521

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.14.git18450f4
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.13.git18450f4
- Update provided packages
  related: #1250521

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.12.git18450f4
- Bump to upstream 18450f4e95c7e76ce3a5dc3a8cb7178ab6d56121
  related: #1250521

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.gitfc402b0
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitfc402b0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.9.gitfc402b0
- Fix runtime dependency on devel
  related: #1250521

* Wed Aug 19 2015 jchaloup <jchaloup@redhat.com> - 0-0.8.gitfc402b0
- Update spec file to spec-2.0
  resolves: #1250521

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.gitfc402b0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.gitfc402b0
- fix provides
  related: #1141841

* Thu Mar 26 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.gitfc402b0
- add devel subpackage for code.google.com/p/... import path (for back-compatibility)
  related: #1141841

* Fri Jan 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.gitfc402b0
- update to fc402b0d6f2a46ba7dcf0a4606031f45fb82a728
  related: #1141841

* Fri Nov 14 2014 Eric Paris <eparis@redhat.com> - 0-0.3.alpha.hg98c781851970
- update to 98c78185197025f935947caac56a7b6d022f89d2

* Mon Sep 15 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.alpha.hge1c259484b49
- update to e1c259484b495133836706f46319f5897f1e9bf6
- preserve timestamps of copied files

* Mon Aug 04 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.1.alpha.hg0923cdda5b82
- First package for Fedora.

