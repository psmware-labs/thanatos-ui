#  SPDX-License-Identifier: AGPL-3.0-only

#  Copyright (C) 2021  Patrick McLean - psmware ltd

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
FROM psmwareltd/dj-node:1.0
LABEL author="Pat McLean" \
      maintainer="Pat McLean<github@psmware.ie>"

COPY .devcontainer/bin /home/vscode/bin
RUN chown -fR vscode.vscode /home/vscode/bin
RUN chmod -fR 700 /home/vscode/bin