/** @odoo-module */

import { registry } from "@web/core/registry";
import { download } from "@web/core/network/download";

async function executeAccountReportDownload({ env, action }) {
  env.services.ui.block();
  const url = "/custom_account_reports";
  const data = action.data;
  try {
    await download({ url, data });
    env.services.action.doAction({ type: 'ir.actions.act_window_close' });
  } finally {
    env.services.ui.unblock();
  }
}

registry
  .category("action_handlers")
  .add('ir_actions_account_report_download', executeAccountReportDownload);
