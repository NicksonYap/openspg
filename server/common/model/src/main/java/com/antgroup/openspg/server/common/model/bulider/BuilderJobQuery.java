/*
 * Copyright 2023 OpenSPG Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied.
 */
package com.antgroup.openspg.server.common.model.bulider;

import java.util.Date;
import java.util.List;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class BuilderJobQuery extends BuilderJob {

  private static final long serialVersionUID = 7320973107956820414L;

  private List<Long> ids;

  private Date startCreateTime;

  private Date endCreateTime;

  private Integer pageNo;

  private Integer pageSize;

  private String sort;

  private String order;

  private String keyword;
}
